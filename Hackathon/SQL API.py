import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect("Hackathon.db")
    except Error as e:
        print(e)
    return conn

#returns a {Topic: {Subtopic: {String[][]} } }
'''def VideosFromUser(username):
    tmp = {}
    conn = create_connection()
    topics = TopicsFromUser(conn,username)
    for topic in topics:
        tmpd1 = {}
        subtopics = getSubTopicsFromTopic(conn,topic)
        for subtopic in subtopics:
            videos = getLinksFromSubTopic(conn,subtopic)
            tmpd1[subtopic] = videos
        tmp[topic] = tmpd1
    
    return tmp'''

def addSubTopic(conn,subtopic,videoInfos):
    cur = conn.cursor()
    cur.execute("INSERT INTO SubTopics(SubTopic) VALUES(?)", (subtopic))
    conn.commit()
    STID = cur.rowlastid
    for videoInfo in videoInfos:
        LID = addLink(conn,videoInfo)
        addContent(conn,STID,LID)
    return STID

def addLink(conn,videoInfo):
    cur = conn.cursor()
    cur.execute("INSERT INTO Links(Title,Link) VALUES(?)", (videoInfo[0],videoInfo[1]))
    conn.commit()
    return cur.lastrowid

def addContent(conn,STID,LID):
    cur = conn.cursor()
    cur.execute("INSERT INTO Content(STID,LID) VALUES(?)", (STID,LID))
    conn.commit()

def addStInT(conn,TID,STID):
    cur = conn.cursor()
    cur.execute("INSERT INTO StInT(TID,STID) VALUES(?)", (TID,STID))
    conn.commit()

def TopicsFromUser(conn,username):
    cur = conn.cursor()
    cur.execute(
    "SELECT Topic FROM Topics WHERE TID in "+
        "(SELECT TID FROM Progress WHERE AID = "+
            "(SELECT AID FROM Accounts WHERE UserName = ?)"+
        ")"
    ,(username,))
    return reformatResultSet(cur.fetchall())

#1 Result query only
def reformatResultSet(rs):
    arr = []
    for tuple in rs:
        arr.append(tuple[0])
    return arr

#Multiple Results per row
def reformatMResultSet(rs):
    arr = []
    for tuple in rs:
        arr2 = []
        #print(tuple)
        for elem in tuple:
            arr2.append(elem)
        arr.append(arr2)
    return arr

def getLinksFromSubTopic(conn,subtopic):
    cur = conn.cursor()
    cur.execute(
    "SELECT Title,Link FROM Links WHERE LID in"+
        "(SELECT LID FROM Content WHERE STID in"+
            "(SELECT STID FROM SubTopics WHERE SubTopic = ?))"
    ,(subtopic,))
    return reformatMResultSet(cur.fetchall())

def getSubTopicsFromTopic(conn,topic):
    cur = conn.cursor()
    cur.execute(
    "SELECT SubTopic FROM SubTopics WHERE STID in"+
        "(SELECT STID FROM StInT WHERE TID in"+
            "(SELECT TID FROM Topics WHERE Topic = ?))"
    ,(topic,))
    return reformatResultSet(cur.fetchall())

##BELOW METHODS ARE ONLY ONES THAT NEED TO BE CALLED EXTERNALLY
def authenticate(username,password):
    cur = create_connection().cursor()
    cur.execute("SELECT UserName FROM Accounts WHERE UserName =? AND Password=?",(username,password))
    return cur.fetchone() != None

def addUser(username,password):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO Accounts(UserName,Password) VALUES(?,?)", (username,password))
    conn.commit()

def watched(username,id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT LID FROM Links where Link = ?",(id,))
    LID = cur.fetchone()[0]
    cur.execute("SELECT AID FROM Accounts where UserName = ?",(username,))
    AID = cur.fetchone()[0]
    cur.execute("INSERT INTO Watched(AID,LID) VALUES(?,?)", (AID,LID))
    conn.commit()

#topic: String
#subtopics: String[] 
#videoInfos: {String: String[][]}  subtopic is key to a list of lists, 
def addTopic(topic,subtopics,videoInfos):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO Topics(Topic) VALUES(?)", (topic))
    conn.commit()
    TID = cur.rowlastid
    for subtopic in subtopics:
        STID = addSubTopic(conn,subtopic,videoInfos[subtopic])
        addStInT(conn,TID,STID)
    return TID

def VideosFromUser(username):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute('''
        SELECT l.Title, l.Link, t.Topic, st.SubTopic
        FROM Links l
        JOIN Content c ON c.LID = l.LID
        JOIN SubTopics st ON st.STID = c.STID
        JOIN StInT si ON si.STID = st.STID
        JOIN Topics t ON t.TID = si.TID
        JOIN Progress p ON p.TID = t.TID
        JOIN Accounts a ON a.AID = p.AID
        WHERE a.UserName = 'user' AND l.LID NOT IN (
        SELECT w.LID FROM Watched w 
        JOIN Accounts a ON a.AID = w.AID
        WHERE a.UserName = ?)
    ''',(username,))
    return reformatMResultSet(cur.fetchall())
