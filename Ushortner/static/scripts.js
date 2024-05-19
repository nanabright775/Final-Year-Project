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
