from matplotlib import pyplot as plt


def main():
    students = ["John", "Naitik", "Mummy", "Papa", "Nishant"]
    scores = [85, 90, 78, 92, 88]

    figure, (bar_axis, pie_axis) = plt.subplots(1, 2, figsize=(10, 5))

    bar_axis.bar(students, scores, color="skyblue")
    bar_axis.set_title("Student scores")
    bar_axis.set_ylabel("Score")
    bar_axis.tick_params(axis="x", rotation=30)

    pie_axis.pie(scores, labels=students, autopct="%1.1f%%")
    pie_axis.set_title("Score distribution")

    figure.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()