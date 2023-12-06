import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { quasar, transformAssetUrls } from '@quasar/vite-plugin'
import { fileURLToPath, URL } from 'node:url'
import { Notify } from 'quasar'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue({
    template: { transformAssetUrls }
    }),
    quasar({
      sassVariables: 'src/quasar-variables.sass',
    }),
    'Notify'
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('src', import.meta.url))
    }
  }
})
