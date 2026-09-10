from datetime import datetime
import requests  # type: ignore[reportMissingModuleSource]


def fetch_data():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    if response.status_code == 200:
        return response.json()

    return {}


def generate_log(log_data):
    if not isinstance(log_data, list):
        raise ValueError("Log data must be a list.")

    # Only fetch data if the log list is not empty
    if log_data:
        post = fetch_data()

        if post:
            log_data.append(
                f"Fetched Post Title: {post.get('title')}"
            )

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")

    return filename


if __name__ == "__main__":
    log_data = [
        "User logged in",
        "User updated profile",
        "Report exported"
    ]

    generate_log(log_data)