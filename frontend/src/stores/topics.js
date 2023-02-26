import { defineStore } from "pinia";

export const useTopicsStore = defineStore("topics", {
    state: () => ({ topics: [], selectedTopic: {} }),
    actions: {
        reformatFromServer(output) {
            // refashion output to something we understand
            let listBuilder = [];
            output.topicnames.forEach(name => {
                let objectBuilder = {};
                let totalWatched = 0;
                let totalVideos = 0;
                objectBuilder['name'] = name;
                objectBuilder['subtopics'] = []
                let subtopics = output['topics'][name].subtopicnames;

                subtopics.forEach(subtopicname => {
                    let videos = output['topics'][name][subtopicname];
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
            return listBuilder;
        },
        updateTopicsFromResponse(response) {
            this.topics = this.reformatFromServer(response.data);
        },
        setWatched(linkId) {
            // NOTE: frontend implementation to look smooth
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
