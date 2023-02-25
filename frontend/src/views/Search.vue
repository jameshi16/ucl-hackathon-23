<script setup></script>

<template>
  <main>
    <div id="header-bar">
      <div id="user-greeting">
        <p>Hi, {{ user }}!</p>
      </div>
    </div>
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
import "@/assets/search.scss";
export default {
  data() {
    return {
      user: "testing",
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
