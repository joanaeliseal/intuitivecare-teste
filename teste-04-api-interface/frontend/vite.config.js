import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    // Remove completamente o DevTools em produção
    // vueDevTools(), 
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
  server: {
    hmr: {
      overlay: false, // Desabilita o overlay de erro (incluindo marca d'água do Vue DevTools)
    },
  },
})
