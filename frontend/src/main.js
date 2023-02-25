import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import UserGreeting from './components/UserGreeting.vue'

import './assets/main.css'

const app = createApp(App)

app.use(router)

app.component('UserGreeting', UserGreeting);

app.mount('#app')
