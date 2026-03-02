document.addEventListener("DOMContentLoaded", function () {

  // nur in Reveal-Präsentationen
  if (!document.body.classList.contains("reveal-viewport")) return;

  if (document.querySelector(".logo-box")) return;

  const box = document.createElement("div");
  box.className = "logo-box";

  box.innerHTML = `
    <img class="logo-img" src="/iWIP/bilder/logo_siblog_iwip.png" alt="SciBlog iWIP">
    <span class="logo-text">SciBlog iWIP</span>
  `;

  // 👇 direkt an BODY anhängen (nicht an .reveal!)
  document.body.appendChild(box);
});