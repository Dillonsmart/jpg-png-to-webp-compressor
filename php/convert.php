<?php

require "constants.php";

$files = array_diff(scandir(ORIGINAL_FILES_DIR), array('.', '..'));
$supportedTypes = ['image/png', 'image/jpeg'];

foreach($files as $file) {

    $file = ORIGINAL_FILES_DIR . $file;
    $image = null;
    $newFilePath = null;

    if(!is_allowed($file)) {
        continue;
    }

    $fileInfo = new finfo(FILEINFO_MIME_TYPE);
    $type = $fileInfo->buffer(file_get_contents($file));

    if(!in_array($type, $supportedTypes)) {
        continue;
    }

    switch($type) {
        case "image/png":
            $image = imagecreatefrompng($file);
            $newFilePath = str_replace("png", "webp", $file);
            break;
        case "image/jpeg":
            $image = imagecreatefromjpeg($file);
            $newFilePath = str_replace("jpeg", "webp", $file);
            break;
        default:
            break;
    }

    imagewebp($image, $newFilePath, CONVERSION_COMPRESSION_QUALITY);

}

function is_allowed($file) {
    if(substr($file, 0, 1) === '.') {
        return false;
    }

    if(is_dir($file)) {
        return false;
    }

    return true;
}
