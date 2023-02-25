<script setup></script>

<template>
  <main>
    <h2>{{ topicName }}</h2>
    <div v-show="percentage < 1" class="completed-card">
      <p>Percentage complete: {{ percentage * 100 }}%</p>
      <button>Continue now</button>
    </div>
    <div v-show="percentage == 1" class="inprogress-card">
      <p>Completed!</p>
      <p>Certification:{{ certificateID }}</p>
    </div>
  </main>
</template>

<script>
export default {
  props: ["percentage", "topicName"],
  data() {
    // TODO: For now, we mock certifications
    return {
      certificateID: this.$CryptoJS
        .SHA256(this.topicName)
        .toString()
        .slice(0, 8),
    };
  },
  components: {},
  methods: {},
};
</script>
