<script setup>
import SubTopic from "./SubTopic.vue";
</script>

<template>
  <main>
    <UserGreeting user="test" />
    <h1>Topic Name</h1>
    <div>
      <div class="subtopics">
        <div v-for="subtopic in mockSubTopics" class="subtopic">
          <SubTopic
            :subtopicName="subtopic.subtopicName"
            :videos="subtopic.videos"
          ></SubTopic>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  data() {
    return {
      mockSubTopics: [
        {
          subtopicName: "Subtopic 1",
          videos: [
            {
              title: "bad apple",
              videoId: "9lNZ_Rnr7Jc",
            },
            {
              title: "bad apple 2",
              videoId: "9lNZ_Rnr7Jc",
            },
          ],
        },
      ],
    };
  },
  components: { SubTopic },
  methods: {},
};
</script>
