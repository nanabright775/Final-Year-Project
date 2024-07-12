/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {
      height: {
        '9rem': '9rem',
      },
    },
  },
  plugins: [
    require('flowbite/plugin'),
    // require('@tailwindcss/aspect-ratio'),
  ],
}

