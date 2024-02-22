self.addEventListener("install", (event) => {
    console.debug("Service worker is installed");
});

self.addEventListener("activate", (event) => {
    console.debug("Service worker is activated");
});

self.addEventListener("fetch", (event) => {
    console.log("Service worker is fetching a resource");
});
