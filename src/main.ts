
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/css/index.css'
import { createPinia } from 'pinia'
import Notifications from '@kyvg/vue3-notification'
import i18n from './i18n'

const app = createApp(App)

app.use(router)
app.use(Notifications)
app.use(i18n)
app.use(createPinia())

app.mount('#app')
