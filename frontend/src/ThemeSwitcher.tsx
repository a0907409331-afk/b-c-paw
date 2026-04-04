import React, { useState } from "react";

const themes = ["cyber", "ios", "dashboard", "luxury", "assistant", "minimal", "card"];

export default function ThemeSwitcher() {
  const [theme, setTheme] = useState(localStorage.getItem("theme") || "cyber");

  const changeTheme = (t: string) => {
    setTheme(t);
    localStorage.setItem("theme", t);
    document.documentElement.setAttribute("data-theme", t);
  };

  return (
    <div>
      <button onClick={() => document.getElementById("themeModal")?.showModal()}>
        🎨 切換風格
      </button>
      <dialog id="themeModal">
        {themes.map(t => (
          <button key={t} onClick={() => changeTheme(t)}>{t}</button>
        ))}
      </dialog>
    </div>
  );
}

