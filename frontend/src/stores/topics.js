import { defineStore } from "pinia";

export const useTopicsStore = defineStore("topics", {
    state: () => ({ topics: [], selectedTopic: {} }),
    actions: {
        fetchTopicsFromUser(username) {
            const exampleOutput =
            {
                "topicnames": [
                    "Object-Oriented Programming",
                    "Calculus"
                ],
                "topics": {
                    "Object-Oriented Programming": {
                        "subtopicnames": [
                            "Abstraction",
                            "Overloading",
                            "Encapsulation"
                        ],
                        "Abstraction": {
                            "Learning Abstraction": {
                                "videoId": "56743tyfgh45",
                                "watched": true
                            },
                            "Learning Abstraction 2": {
                                "videoId": "16789tyfgh45",
                                "watched": false
                            }
                        },
                        "Overloading": {
                            "Learning Overloading": {
                                "videoId": "45789tyfgh45",
                                "watched": false
                            }
                        },
                        "Encapsulation": {
                            "Learning Encapsulation": {
                                "videoId": "67894gtyfgh45",
                                "watched": false
                            }
                        }
                    },
                    "Calculus": {
                        "subtopicnames": [
                            "Differentiation",
                            "Integration"
                        ],
                        "Differentiation": {
                            "Learning Differentiation": {
                                "videoId": "56789t45",
                                "watched": false
                            },
                            "Learning Differentiation 2": {
                                "videoId": "567yfgh45",
                                "watched": true
                            }
                        },
                        "Integration": {
                            "Learning Integration": {
                                "videoId": "56da33rtyfgh45",
                                "watched": true
                            }
                        }
                    }
                }
            };

            // refashion output to something we understand
            let listBuilder = [];
            exampleOutput.topicnames.forEach(name => {
                let objectBuilder = {};
                let totalWatched = 0;
                let totalVideos = 0;
                objectBuilder['name'] = name;
                objectBuilder['subtopics'] = []
                let subtopics = exampleOutput['topics'][name].subtopicnames;

                subtopics.forEach(subtopicname => {
                    let videos = exampleOutput['topics'][name][subtopicname];
                    let watched = 0;
                    let newVideos = Object.keys(videos).map(video => {
                        let newDict = {};
                        newDict['title'] = video;
                        newDict['videoId'] = videos[video]['videoId'];
                        newDict['watched'] = videos[video]['watched'];
                        if (newDict['watched']) {
                            watched++;
                            totalWatched++;
                        }
                        totalVideos++;
                        return newDict;
                    });
                    objectBuilder['subtopics'].push({
                        name: subtopicname,
                        videos: newVideos,
                        percentage: watched / Object.keys(newVideos).length
                    });
                    objectBuilder['percentage'] = totalWatched / totalVideos;
                });
                listBuilder.push(objectBuilder);
            });
            this.topics = listBuilder;
        },
        setWatched(username, linkId) {
            // TODO: make call to set linkID as watched
            // TODO: should call backend again to fetch all the data again

            // NOTE: frontend implementation because i'm lazy
            this.topics.forEach(topic => (
                topic.subtopics.forEach(subtopic => (
                    subtopic['videos'].forEach(video => {
                        if (video.videoId == linkId)
                            video.watched = true;
                    })
                ))
            ));
            this.recalculatePercentages();
        },
        recalculatePercentages() {
            this.topics.forEach(topic => {
                let watched = 0;
                let total = 0;
                topic.subtopics.forEach(subtopic => {
                    let subWatched = 0;
                    let subTotal = 0;

                    subtopic.videos.forEach(video => {
                        if (video.watched) {
                            subWatched++;
                            watched++;
                        }
                        subTotal++;
                        total++;
                    });
                    subtopic['percentage'] = subWatched / subTotal;
                });
                topic['percentage'] = watched / total;
            });

        }
    }
});
