from pyscript import document

grade_7 = {"Raymond Manalansan", "Maya Angeles"}
grade_8 = {"Bernadine Santos", "Jiwon Son"}
grade_9 = {"June Bae", "Chesca Ignacio"}
grade_10 = {"Riona Narciso", "Isa Rivera"}

new_members = set()


def render_roster():
    full_set = grade_7 | grade_8 | grade_9 | grade_10 | new_members

    total_count = len(full_set)

    formatted_members = ", ".join(sorted(full_set))

    output_div = document.querySelector("#output")

    output_div.innerHTML = f"""
        <div class="alert alert-info">
            <h5 class="alert-heading">
                Total Members:
                <span class="badge bg-primary">{total_count}</span>
            </h5>

            <hr>

            <p class="mb-0">
                <strong>Full Member List:</strong><br>
                {formatted_members}
            </p>
        </div>
    """


def add_member(event):
    first = document.querySelector("#first-name").value.strip()
    last = document.querySelector("#last-name").value.strip()

    if first or last:
        new_entry = f"{first} {last}".strip()
        new_members.add(new_entry)

    document.querySelector("#first-name").value = ""
    document.querySelector("#last-name").value = ""

    render_roster()


render_roster()
