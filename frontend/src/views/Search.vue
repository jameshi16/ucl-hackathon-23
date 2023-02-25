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
        topicName="Object Oriented Programming"
        :percentage="0.5"
      ></TopicCard>
    </div>

    <div id="completed-topics">
      <h1>Completed Topics</h1>
      <TopicCard topicName="Abstraction" :percentage="1"></TopicCard>
    </div>
  </main>
</template>

<script>
export default {
  data() {
    return {
      sinput: "",
    };
  },
  methods: {
    doSearch(event) {
      console.log(this.sinput);
    },
  },
  components: {
    TopicCard,
  },
};
</script>
