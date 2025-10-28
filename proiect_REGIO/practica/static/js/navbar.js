document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.querySelector('.hamburger');
    const verticalMenu = document.querySelector('.vertical-menu');
    const menuItems = document.querySelectorAll('.vertical-menu > ul > li');

    function closeAllSubmenus() {
        document.querySelectorAll('.submenu').forEach(submenu => {
            submenu.classList.remove('active', 'clicked');
        });
    }

    hamburger.addEventListener('click', function() {
        hamburger.classList.toggle('active');
        verticalMenu.classList.toggle('expanded');
        
        if (!verticalMenu.classList.contains('expanded')) {
            closeAllSubmenus();
        }
    });

    menuItems.forEach(item => {
        const link = item.querySelector('a');
        const submenu = item.querySelector('.submenu');

        let hoverTimeout;

        item.addEventListener('mouseenter', () => {
            clearTimeout(hoverTimeout);
            hoverTimeout = setTimeout(() => {
                if (!submenu.classList.contains('clicked')) {
                    document.querySelectorAll('.submenu').forEach(menu => {
                        if (menu !== submenu && !menu.classList.contains('clicked')) {
                            menu.classList.remove('active');
                        }
                    });
                    submenu.classList.add('active');
                }
            }, 500); // Shortened hover delay for better UX
        });

        item.addEventListener('mouseleave', () => {
            clearTimeout(hoverTimeout);
            hoverTimeout = setTimeout(() => {
                if (!submenu.classList.contains('clicked')) {
                    submenu.classList.remove('active');
                }
            }, 300);
        });

        link.addEventListener('click', (e) => {
            if (submenu) {
                e.preventDefault();
                if (verticalMenu.classList.contains('expanded')) {
                    submenu.classList.toggle('active');
                    submenu.classList.toggle('clicked');

                    document.querySelectorAll('.submenu').forEach(menu => {
                        if (menu !== submenu && menu.classList.contains('clicked')) {
                            menu.classList.remove('active', 'clicked');
                        }
                    });
                }
            } else {
                window.location.href = link.getAttribute('href');
            }
        });
    });

    // JavaScript to add random emoji
    function addRandomEmoji() {
        const emojis = ['😀', '🎉', '🔥', '💻', '🌟', '🚀', '😊', '🍀', '🌈', '🦄'];
        const randomEmoji = emojis[Math.floor(Math.random() * emojis.length)];
        const welcomeMessageElement = document.querySelector('.welcome-message');
        
        if (welcomeMessageElement) {
            welcomeMessageElement.innerHTML += ` ${randomEmoji}`;
        }
    }

    window.onload = addRandomEmoji;

    document.getElementById("logout").onclick = () => {
        window.location.href = "/logout/";
    };
});
