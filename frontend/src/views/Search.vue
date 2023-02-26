<script setup>
import TopicCard from "./TopicCard.vue";
import Loading from "vue-loading-overlay";

import "@/assets/search.scss";
import "vue-loading-overlay/dist/css/index.css";
</script>

<template>
  <main>
    <div class="vl-parent">
      <loading
        v-model:active="isLoading"
        :is-full-page="fullPage"
        :height="128"
        :width="128"
        :opacity="1.0"
        background-color="pink"
      />
      <UserGreeting :user="logged_in" />
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
    </div>

    <div id="in-progress-topics">
      <h1>Continue your topics</h1>
      <TopicCard
        v-for="(topic, i) in incompleteTopics"
        :topicName="topic.name"
        :id="i"
        :percentage="topic.percentage"
        @triggerClick="onClickContinue"
      ></TopicCard>
    </div>

    <div id="completed-topics">
      <h1>Completed Topics</h1>
      <TopicCard
        v-for="(topic, i) in completeTopics"
        :topicName="topic.name"
        :id="i"
        :percentage="topic.percentage"
        @triggerClick="onClickContinue"
      ></TopicCard>
    </div>
  </main>
</template>

<script>
import { mapWritableState, mapState, mapStores } from "pinia";
import { useAuthStore } from "@/stores/auth";
import { useTopicsStore } from "@/stores/topics";

export default {
  data() {
    return {
      sinput: "",
      isLoading: false,
    };
  },
  mounted() {
    this.getData(this.logged_in);
  },
  methods: {
    doSearch(event) {
      console.log(this.sinput);
      this.isLoading = true;
      // TODO: do something here
      this.isLoading = false;
    },
    getData(username) {
      // TODO: replace with actual call to backend
      this.isLoading = true;
      this.topicsStore.fetchTopicsFromUser(username);
      this.isLoading = false;
    },
    onClickContinue(id) {
      this.selectedTopic = this.incompleteTopics[id];
      this.$router.push({ name: "topic" });
    },
  },
  components: {
    TopicCard,
  },
  computed: {
    ...mapState(useAuthStore, ["logged_in"]),
    ...mapStores(useTopicsStore),
    ...mapWritableState(useTopicsStore, ["topics", "selectedTopic"]),
    completeTopics() {
      return this.topics.filter((topic) => topic.percentage >= 1);
    },
    incompleteTopics() {
      return this.topics.filter((topic) => topic.percentage < 1);
    },
  },
};
</script>
