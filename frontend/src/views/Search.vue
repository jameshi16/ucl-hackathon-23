<script setup>
import TopicCard from "./TopicCard.vue";
import Loading from "vue-loading-overlay";

import "@/assets/search.scss";
import "vue-loading-overlay/dist/css/index.css";
</script>

<template>
  <main id="dashboard">
    <div class="vl-parent">
      <loading
        v-model:active="isLoading"
        :is-full-page="fullPage"
        :height="128"
        :width="128"
        :opacity="1.0"
        background-color="white"
      />
      <UserGreeting :user="logged_in" />
    </div>

    <div class="dashboard-cont">
      <section id="search">
        <h1>Start a New Journey</h1>
        <form id="search-cont" onsubmit="return false;">
          <button @click="doSearch">Search</button>
          <input
            type="text"
            placeholder="What do you want to learn?"
            v-model="sinput"
          />
        </form>
      </section>

      <section v-if="incompleteTopics.length !== 0" id="in-progress">
        <h1>Continue Learning</h1>
        <div class="topic-cont">
          <TopicCard
            v-for="(topic, i) in incompleteTopics"
            :topicName="topic.name"
            :id="i"
            :percentage="topic.percentage"
            @triggerClick="onClickContinue"
          ></TopicCard>
        </div>
      </section>

      <section v-if="completeTopics.length !== 0" id="completed">
        <h1>Completed Topics</h1>
        <div class="topic-cont">
          <TopicCard
            v-for="(topic, i) in completeTopics"
            :topicName="topic.name"
            :id="i"
            :percentage="topic.percentage"
            @triggerClick="onClickContinue"
          ></TopicCard>
        </div>
      </section>
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
      this.isLoading = true;
      this.$http
        .post(this.$backendUrl + this.$apiChoice, null, {
          params: {
            username: this.logged_in,
            topic: this.sinput,
          },
        })
        .then(() => {
          this.$nextTick(() => {
            this.getData(this.logged_in);
          });
        })
        .finally(() => {
          this.isLoading = false;
        });
    },
    getData(username) {
      this.isLoading = true;
      this.$http
        .post(this.$backendUrl + "user/savedtopicsapi", null, {
          params: {
            username: this.logged_in,
          },
        })
        .then((response) => {
          this.topics.$state =
            this.topicsStore.updateTopicsFromResponse(response);
        })
        .finally(() => {
          this.isLoading = false;
        });
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
