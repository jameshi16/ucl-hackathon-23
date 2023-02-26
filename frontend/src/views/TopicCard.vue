<script setup></script>

<template>
  <div class="topic-card">
    <h2>{{ topicName }}</h2>
    <div v-show="percentage < 1" class="completed-card">
      <p>Percentage complete: {{ percentage * 100 }}%</p>
      <button @click="$emit('triggerClick', id)">Continue Now</button>
    </div>
    <div v-show="percentage == 1" class="inprogress-card">
      <p>Completed!</p>
      <p>Certification:{{ certificateID }}</p>
    </div>
  </div>
</template>

<script>
export default {
  props: ["id", "percentage", "topicName"],
  data() {
    // TODO: For now, we mock certifications
    return {
      certificateID: this.$CryptoJS
        .SHA256(this.topicName)
        .toString()
        .slice(0, 8),
    };
  },
  methods: {},
  components: {},
};
</script>
