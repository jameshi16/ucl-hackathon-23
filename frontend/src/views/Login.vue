<script setup>
import Loading from "vue-loading-overlay";
import "vue-loading-overlay/dist/css/index.css";
</script>

<template>
  <main id="login-view">
    <loading
      v-model:active="isLoading"
      :is-full-page="fullPage"
      :height="128"
      :width="128"
      :opacity="1.0"
      background-color="black"
    />
    <h1>LearnFaster</h1>
    <form id="login-form" onsubmit="return false;">
      <input type="text" v-model="username" placeholder="Username" />
      <input type="password" v-model="password" placeholder="Password" />
      <button @click="login">Login</button>
      <p
        class="error"
        :style="{ visibility: err_login_failed ? 'visible' : 'hidden' }"
      >
        Error: invalid username or password
      </p>
    </form>
  </main>
</template>

<script>
import { mapWritableState } from "pinia";
import { useAuthStore } from "@/stores/auth";

export default {
  methods: {
    login() {
      this.isLoading = true;
      this.$http
        .post(this.$backendUrl + "user/authapi", null, {
          params: {
            username: this.username,
            password: this.password,
          },
        })
        .then((response) => {
          if (response.data["message"] == "success") {
            this.logged_in = this.username;
            this.$router.push("/search");
          } else {
            this.err_login_failed = true;
          }
        })
        .catch(() => {
          this.err_login_failed = true;
        })
        .finally(() => {
          this.isLoading = false;
        });
    },
  },
  data() {
    return {
      err_login_failed: false,
      isLoading: false,
      username: "",
      password: "",
    };
  },
  computed: {
    ...mapWritableState(useAuthStore, ["logged_in"]),
  },
};
</script>
