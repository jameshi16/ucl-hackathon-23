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
          <input type="text" />
          <div id="search-btn">
            <button>Teach me senpai</button>
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
    };
  },
};
</script>
