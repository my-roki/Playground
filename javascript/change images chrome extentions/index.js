const imageUrl =
  "https://w.namu.la/s/d72c2235c488e3a4c85f891c12791c7cd0fdbba83023d29dc3d654b8c74c2384684115efed97513898771db5fefe39fbae7101c8dba848088a29a0124319709f9ef2c31a233dd5e910d8f1388a4449b933026cfa474b73f20f719f0d01dec33e147e6268e3a632dd07871f8d9ccf3327";

const imageChange = () => {
  const images = document.querySelectorAll("img");
  const iframes = document.querySelectorAll("iframe");

  images.forEach((image) => {
    image.src = imageUrl;
  });
  iframes.forEach((iframe) => {
    const iframeImages = iframe.contentWindow.document.querySelectorAll("img");
    iframeImages.forEach((image) => {
      image.src = imageUrl;
    });
  });
};

const bgImageChange = () => {
  const allTag = document.querySelectorAll("*");

  allTag.forEach((el) => {
    const exists = getComputedStyle(el).backgroundImage !== "none";
    if (exists) {
      el.style.backgroundImage = imageUrl;
    }
  });
};

setInterval(imageChange, 500);
setInterval(bgImageChange, 500);
