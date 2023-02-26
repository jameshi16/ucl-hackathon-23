<script setup>
import SubTopic from "./SubTopic.vue";
</script>

<template>
  <main>
    <div class="vl-parent">
      <UserGreeting user="test" />
      <h1>{{ selectedTopic.name }}</h1>
      <div>
        <div class="subtopics">
          <div v-for="subtopic in selectedTopic.subtopics" class="subtopic">
            <SubTopic
              :subtopicName="subtopic.name"
              :videos="subtopic.videos"
              :percentage="subtopic.percentage"
              @watched="setWatched"
            ></SubTopic>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import { mapState, mapStores } from "pinia";
import { useTopicsStore } from "@/stores/topics";

export default {
  data() {
    return {};
  },
  components: { SubTopic },
  methods: {
    setWatched(video) {
      this.topicsStore.setWatched(undefined, video.videoId);
      this.checkUserDone();
    },
    checkUserDone() {
      if (this.userIsDone) {
        this.$router.push("/search");
      }
    },
  },
  computed: {
    ...mapState(useTopicsStore, ["selectedTopic"]),
    ...mapStores(useTopicsStore),
    userIsDone() {
      return this.selectedTopic.percentage >= 1;
    },
  },
};
</script>
