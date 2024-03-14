from flask import url_for


def get_scan_files_with_details(files):
    response_files = []

    for file in files:
        download_url = url_for("api.scan_files.download_scan_file", uuid=file.uuid, _external=True)
        preview_url = url_for("api.scan_files.scan_file_preview", uuid=file.uuid, _external=True)
        thumbnail_url = url_for("api.scan_files.scan_file_preview", uuid=file.uuid, thumbnail=1, _external=True)

        file_data = dict(**file.__dict__,
                         image={
                             "download_url": download_url,
                             "preview_url": preview_url,
                             "thumbnail_url": thumbnail_url,
                         },
                         details={
                             "width": file.width,
                             "height": file.height,
                             "size": file.size,
                         })

        response_files.append(file_data)

    return response_files
