<script setup>
import "@/assets/search.scss";
import TopicCard from "./TopicCard.vue";
</script>

<template>
  <main>
    <UserGreeting user="test" />
    <div id="search-div">
      <h1>What do you want to learn?</h1>
      <div id="search-inner-div">
        <div id="search-bar">
          <input
            v-model="sinput"
            type="text"
            placeholder="What do you want to learn?"
          />
          <div id="search-btn">
            <button @click="doSearch" id="search-actual-btn">
              Teach me senpai
            </button>
          </div>
        </div>
      </div>
    </div>

    <div id="in-progress-topics">
      <h1>Continue your topics</h1>
      <TopicCard
        v-for="(topic, i) in getIncompleteTopics()"
        :topicName="topic.name"
        :id="i"
        :percentage="topic.percentage"
        @triggerClick="onClickContinue"
      ></TopicCard>
    </div>

    <div id="completed-topics">
      <h1>Completed Topics</h1>
      <TopicCard
        v-for="(topic, i) in getCompleteTopics()"
        :topicName="topic.name"
        :id="i"
        :percentage="topic.percentage"
        @triggerClick="onClickContinue"
      ></TopicCard>
    </div>
  </main>
</template>

<script>
export default {
  data() {
    // TODO: topics is what we would get from backend
    return {
      sinput: "",
      topics: [
        {
          name: "Object Oriented Programming",
          percentage: 0.5,
          subtopics: [
            {
              name: "Abstraction",
              percentage: 0.24,
              videoId: "UkgK8eUdpAo",
            },
            {
              name: "Another Topic",
              percentage: 0.86,
              videoId: "UkgK8eUdpAo",
            },
          ],
        },
        {
          name: "Another Thing To Talk About",
          percentage: 1,
          subtopics: [
            {
              name: "B R U H",
              percentage: 0.24,
              videoId: "UkgK8eUdpAo",
            },
            {
              name: "Okie",
              percentage: 0.86,
              videoId: "UkgK8eUdpAo",
            },
          ],
        },
      ],
    };
  },
  methods: {
    doSearch(event) {
      console.log(this.sinput);
      // TODO: do something here
    },
    getData(username) {
      // TODO: do something here
    },
    onClickContinue(id) {
      // navigate to topic
      //this.$router.push("/topic", params: {});
    },
    getCompleteTopics() {
      return this.topics.filter((topic) => {
        return topic.percentage >= 1;
      });
    },
    getIncompleteTopics() {
      return this.topics.filter((topic) => {
        return topic.percentage < 1;
      });
    },
  },
  components: {
    TopicCard,
  },
};
</script>
