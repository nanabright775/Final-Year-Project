function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(function() {
        alert('URL copied to clipboard!');
    }, function(err) {
        alert('Failed to copy URL: ', err);
    });
}

function copyImageToClipboard(imageSrc) {
    fetch(imageSrc)
        .then(response => response.blob())
        .then(blob => {
            const item = new ClipboardItem({ "image/png": blob });
            navigator.clipboard.write([item]).then(function() {
                alert('QR Code copied to clipboard!');
            }, function(err) {
                alert('Failed to copy QR Code: ', err);
            });
        });
}

function shareToWhatsApp(url) {
    window.open(`https://wa.me/?text=${encodeURIComponent(url)}`, '_blank');
}

function shareToFacebook(url) {
    window.open(`https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}`, '_blank');
}

function shareToTwitter(url) {
    window.open(`https://twitter.com/intent/tweet?url=${encodeURIComponent(url)}`, '_blank');
}

function shareQrCodeToWhatsApp(imageSrc) {
    const imgTag = `<img src="${imageSrc}" alt="QR Code">`;
    window.open(`https://wa.me/?text=${encodeURIComponent(imgTag)}`, '_blank');
}

function shareQrCodeToFacebook(imageSrc) {
    const imgTag = `<img src="${imageSrc}" alt="QR Code">`;
    window.open(`https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(imgTag)}`, '_blank');
}

function shareQrCodeToTwitter(imageSrc) {
    const imgTag = `<img src="${imageSrc}" alt="QR Code">`;
    window.open(`https://twitter.com/intent/tweet?url=${encodeURIComponent(imgTag)}`, '_blank');
}

document.addEventListener('DOMContentLoaded', function () {
    const sidebarItems = document.querySelectorAll('.sidebar-item');

    sidebarItems.forEach(item => {
        item.addEventListener('click', function () {
            sidebarItems.forEach(i => i.classList.remove('bg-gray-100', 'dark:bg-gray-700', 'text-blue-600', 'dark:text-blue-400'));
            this.classList.add('bg-gray-100', 'dark:bg-gray-700', 'text-blue-600', 'dark:text-blue-400');
        });
    });
});



//this is script is for message details
  const messageContainer = document.querySelector('.flex-1');
  const scrollButton = document.getElementById('scrollButton');

  // Show or hide the scroll button based on scroll position
  messageContainer.addEventListener('scroll', () => {
    if (messageContainer.scrollTop + messageContainer.clientHeight < messageContainer.scrollHeight) {
      scrollButton.classList.remove('hidden');
    } else {
      scrollButton.classList.add('hidden');
    }
  });

  // Function to scroll to the bottom
  function scrollToBottom() {
    messageContainer.scrollTop = messageContainer.scrollHeight;
  }

  // Scroll to the bottom initially when the page loads
  window.addEventListener('load', scrollToBottom);


  document.getElementById('downloadBtn').addEventListener('click', function() {
    html2canvas(document.getElementById('business-card')).then(function(canvas) {
        const link = document.createElement('a');
        link.href = canvas.toDataURL('image/png');
        link.download = '{{ business_card.name }}_business_card.png';
        link.click();
    });
});

document.getElementById('shareBtn').addEventListener('click', function() {
    if (navigator.share) {
        navigator.share({
            title: '{{ business_card.name }}\'s Business Card',
            text: 'Check out this business card!',
            url: window.location.href
        }).catch(error => console.error('Error sharing:', error));
    } else {
        alert('Your browser does not support the Web Share API.');
    }
}); 



//stealed code here

const openModalButtons = document.querySelectorAll('[data-modal-target]')
const closeModalButtons = document.querySelectorAll('[data-close-button]')
const overlay = document.getElementById('overlay')

openModalButtons.forEach(button => {
    button.addEventListener('click', () => {
        const modal = document.querySelector(button.dataset.modalTarget)
        openModal(modal)
    })
})

overlay.addEventListener('click', () => {
    const modals = document.querySelectorAll('.modal.active')
    modals.forEach(modal => {
        closeModal(modal)
    })
})

closeModalButtons.forEach(button => {
    button.addEventListener('click', () => {
        const modal = button.closest('.modal')
        closeModal(modal)
    })
})

function openModal(modal){
    if(modal == null) return
    modal.classList.add('active')
    overlay.classList.add('active')
}

function closeModal(modal){
    if(modal == null) return
    modal.classList.remove('active')
    overlay.classList.remove('active')
}

function toggleDropdown() {
    const dropdownMenu = document.getElementById('dropdown-menu');
    dropdownMenu.classList.toggle('hidden');
  }

  document.querySelectorAll("[id^=dropdownMenuButton]").forEach(button => {
    button.addEventListener("click", function() {
        const menuId = this.id.replace("Button", "");
        document.getElementById(menuId).classList.toggle("hidden");
    });
});

