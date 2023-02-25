<script setup>
import "@/assets/usergreeting.scss";
</script>

<template>
  <div id="header-bar">
    <div id="user-greeting">
      <p>Hi, {{ user }}!</p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    user: String,
  },
  data() {
    return {};
  },
  methods: {},
};
</script>
