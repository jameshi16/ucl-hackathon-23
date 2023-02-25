<script setup>
import "@/assets/search.scss";
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
};
</script>
