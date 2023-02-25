<script setup></script>

<template>
  <main id="login-view">
    <h1>Hello Wolrd</h1>
    <form id="login-form" onsubmit="return false;">
      <p
        class="error"
        :style="{ visibility: err_login_failed ? 'visible' : 'hidden' }"
      >
        Error: invalid username or password
      </p>
      <input type="text" placeholder="Username" />
      <input type="password" placeholder="Password" />
      <button @click="login">Login</button>
    </form>
  </main>
</template>

<script>
export default {
  methods: {
    login() {
      this.err_login_failed = true;
    },
  },
  data() {
    return {
      err_login_failed: false,
    };
  },
};
</script>
