/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
      "./index.html",
      "./src/**/*.{vue,js,ts,jsx,tsx}",
    ],
    theme: {
      extend: {
        fontFamily: {
          sans: ['Poppins', 'sans-serif'],
        },
        colors: {
          primary: '#1E40AF',
          'primary-dark': '#1E3A8A',
          destaque: '#26D07C',
          cinza: '#F5F5F5'
        }
      },
    },
    plugins: [],
  }
  