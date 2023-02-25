import { defineStore } from "pinia";

export const useAuthStore = defineStore("auth", {
    state: () => ({ logged_in: null }),
});
