<script setup>
import "vueperslides/dist/vueperslides.css";
import "@/assets/subtopic.scss";
import playpng from "@/assets/play.png";
</script>

<template>
  <main>
    <div>
      <h2>{{ subtopicName }}</h2>
      <div v-show="!noMoreVideos" class="ex--center-mode">
        <p>Percentage done: {{ percentageDone }}</p>
        <vueper-slides
          class="no-shadow"
          arrows-outside
          bullets-outside
          transition-speed="250"
          :dragging-distance="200"
          :touchable="false"
          @slide="changeSlide($event)"
        >
          <vueper-slide
            v-for="(slide, i) in slides"
            :key="i"
            :image="slide.image"
            :link="slide.link"
            openInNew="true"
          >
            <template #content>
              <div class="play-btn">
                <img :src="playpng" />
              </div>
            </template>
          </vueper-slide>
        </vueper-slides>
        <div v-show="!noMoreVideos" class="activeSlide">
          <p>Video Title: {{ currentTitle }}</p>
          <button class="finish-watching" @click="finishWatching($event)">
            Finish Watching
          </button>
        </div>
      </div>
      <div v-show="noMoreVideos">
        <p>You have completed this subtopic!</p>
      </div>
    </div>
  </main>
</template>

<script>
import { VueperSlides, VueperSlide } from "vueperslides";
export default {
  props: ["subtopicName", "videos", "percentage"],
  data() {
    return {
      percentageDone: this.percentage,
      currentIndex: 0,
      currentTitle: "",
      noMoreVideos: false,
      slides: [],
    };
  },
  mounted() {
    if (this.onlyWatched.length > 0) {
      this.currentTitle = this.onlyWatched[0]["title"];
    }
    this.noMoreVideos = this.onlyWatched.length == 0;
    this.slides = this.onlyWatched.map((video) => {
      return {
        title: video["title"],
        image:
          "https://i.ytimg.com/vi/" + video["videoId"] + "/maxresdefault.jpg",
        link: "https://www.youtube.com/watch?v=" + video["videoId"],
      };
    });
  },
  components: { VueperSlides, VueperSlide },
  methods: {
    changeSlide(event) {
      this.currentIndex = event.currentSlide.index;
      this.currentTitle = this.onlyWatched[this.currentIndex].title;
    },
    finishWatching(event) {
      this.$emit("watched", this.onlyWatched[this.currentIndex]);
      this.slides.pop(this.currentIndex);
      if (this.slides.length == 0) {
        this.noMoreVideos = true;
      }
    },
  },
  computed: {
    onlyWatched() {
      return this.videos.filter((video) => !video.watched);
    },
  },
};
</script>
