# Real-Time Clock

## Overview

[🔵 **Live Demo — Visit Site**: Real Time Clock](https://adanhammod.pythonanywhere.com/)

This project is a real-time digital clock with a mini calendar. Users can:

- View current time and date.
- Select a timezone to display the correct time.
- Toggle between Light and Dark mode.
- See the current month with today highlighted.

## Technologies Used

- **HTML/CSS**: Structure and styling, with Flexbox and Grid for layout.
- **JavaScript**:
  - Fetch current time from a server API.
  - Update the clock every second.
  - Build the calendar dynamically.
  - Handle timezone selection and dark mode toggle.

## Features

1. **Real-Time Clock**: Updates every second, shows `HH:MM:SS`.
2. **Mini Calendar**: Displays current month, highlights today.
3. **Timezone Support**: User can select different timezones.
4. **Dark/Light Mode**: Button toggles the theme for better accessibility.
5. **Responsive Layout**: Uses Flexbox to align clock and calendar side by side and wrap on smaller screens.

## Code Structure

- **index.html**: Main page with clock and calendar containers.
- **CSS**: Styling for light/dark modes, button colors, hover effects, calendar grid.
- **JavaScript**:
  - `updateTime()` fetches and updates time & date.
  - `buildCalendar()` dynamically creates the calendar.
  - Event listeners for timezone selection and dark mode toggle.

## Notes

- Buttons and calendar days are styled for hover effects and interactivity.
- Uses semi-transparent backgrounds and blur to enhance readability on background image.
- The project is designed to be easily extendable (e.g., adding events to the calendar).

![1763390605077](image/report/1763390605077.png)
