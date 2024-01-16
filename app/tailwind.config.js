/** @type {import('tailwindcss').Config} */

module.exports = {
  content: ['./pages/**/*.{js,ts,jsx,tsx}', './components/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      fontFamily: {
      'league': ['League Spartan', 'sans-serif'],
      'poppins': ['Poppins','sans-serif'],
      'montserrat': ['Montserrat','sans-serif']
    },
    backgroundColor: {

    },
    colors: {

    }
  },
  },
  plugins: [
    [require('@tailwindcss/forms')],
    [require('tailwind-scrollbar')],
    [require('@tailwindcss/typography')],
  ],
}
