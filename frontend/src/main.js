import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

import { Quasar } from 'quasar'

// Import icon libraries
import '@quasar/extras/roboto-font/roboto-font.css'
import '@quasar/extras/material-icons/material-icons.css'
import '@quasar/extras/fontawesome-v6/fontawesome-v6.css'

// Import Quasar css
import 'quasar/dist/quasar.css'
import { Notify } from "quasar";

import router from './router.js'

const app = createApp(App)
app.use(Quasar, {
    plugins: [Notify], // import Quasar plugins and add here
})
app.use(router)
app.mount('#app')
