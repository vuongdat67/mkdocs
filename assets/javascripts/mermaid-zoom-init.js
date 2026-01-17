document.addEventListener("DOMContentLoaded", () => {
  mermaid.initialize({
    startOnLoad: true,
    theme: "neutral",
    securityLevel: "loose",
    flowchart: { useMaxWidth: true },
    zoom: {
      maxScale: 4,
      minScale: 0.5
    }
  });

  // Apply zoom plugin to all Mermaid diagrams
  if (window.mermaidZoom) {
    window.mermaidZoom.initialize({ zoom: 0.8 });
  }
});
