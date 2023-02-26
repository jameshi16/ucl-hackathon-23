<template>
  <main id="login-view">
    <h1>Hello World</h1>
    <form id="login-form" onsubmit="return false;">
      <p
        class="error"
        :style="{ visibility: err_login_failed ? 'visible' : 'hidden' }"
      >
        Error: invalid username or password
      </p>
      <input type="text" v-model="username" placeholder="Username" />
      <input type="password" v-model="password" placeholder="Password" />
      <button @click="login">Login</button>
    </form>
  </main>
</template>

<script>
import { mapWritableState } from "pinia";
import { useAuthStore } from "@/stores/auth";

export default {
  methods: {
    login() {
      if (this.username === "ollie" && this.password === "password") {
        this.logged_in = this.username;
        this.$router.push("/search");
      } else {
        this.err_login_failed = true;
      }
    },
  },
  data() {
    return {
      err_login_failed: false,
    };
  },
  computed: {
    ...mapWritableState(useAuthStore, ["logged_in"]),
  },
};
</script>
