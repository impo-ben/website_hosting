//console.log("Counter JS Loaded");
document.addEventListener("DOMContentLoaded", () => {

    const counters = document.querySelectorAll(".counter");

    const observer = new IntersectionObserver((entries) => {

        entries.forEach(entry => {

            if (!entry.isIntersecting) return;

            const counter = entry.target;

            // Prevent multiple animations
            if (counter.dataset.animated === "true") return;

            counter.dataset.animated = "true";

            const target = parseInt(counter.dataset.target);
            const suffix = counter.dataset.suffix || "";

            let current = 0;

            const duration = 2000; // 2 seconds
            const fps = 60;
            const totalFrames = duration / (1000 / fps);
            const increment = target / totalFrames;

            function updateCounter() {

                current += increment;

                if (current < target) {

                    counter.textContent = Math.floor(current) + suffix;

                    requestAnimationFrame(updateCounter);

                } else {

                    counter.textContent = target + suffix;

                }

            }

            updateCounter();

        });

    }, {
        threshold: 0.3
    });

    counters.forEach(counter => observer.observe(counter));

});