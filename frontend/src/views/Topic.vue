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
              :key="refreshSubtopics"
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
import { useAuthStore } from "@/stores/auth";
import { useTopicsStore } from "@/stores/topics";

export default {
  data() {
    return { refreshSubtopics: false };
  },
  components: { SubTopic },
  methods: {
    setWatched(video) {
      this.$http.post(this.$backendUrl + "user/watchedapi", null, {
        params: {
          username: this.logged_in,
          video_id: video.videoId,
        },
      }),
        this.topicsStore.setWatched(video.videoId);
      this.$nextTick(() => {
        this.refreshSubtopics = !this.refreshSubtopics;
      });
      this.checkUserDone();
    },
    checkUserDone() {
      if (this.userIsDone) {
        this.$router.push("/search");
      }
    },
  },
  computed: {
    ...mapState(useAuthStore, ["logged_in"]),
    ...mapState(useTopicsStore, ["selectedTopic"]),
    ...mapStores(useTopicsStore),
    userIsDone() {
      return this.selectedTopic.percentage >= 1;
    },
  },
};
</script>
