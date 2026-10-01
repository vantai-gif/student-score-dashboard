from io import BytesIO
import matplotlib
matplotlib.use("Agg"
)
import matplotlib.pyplot as plt
import seaborn as sns

def distribution_png(df):
    fig, ax = plt.subplots(figsize=(8, 4.5))
    sns.histplot(data=df, x="total_score", bins=10,
                kde=True, color="#2563eb", ax=ax)
    ax.set_title("Phân phối điểm tổng kết")
    ax.set_ylabel("Số lượng sinh viên")
    fig.tight_layout()

    bufer = BytesIO()
    fig.savefig(bufer, format="png", dpi=140)
    plt.close(fig)
    bufer.seek(0)
    return bufer

#Tạo biểu đồ tương tác Plotly
import plotly.express as px

def classification_chart_html(df):
    counts = (
        df["classification"].astype(str)
        .value_counts()
        .rename_axis("classification")
        .reset_index(name="count")
    )
    fig = px.bar(
        counts, x="classification", y="count",
        color="classification",
        title="So sinh vien theo xep loai"
    )
    fig.update_layout(showlegend=False, height=420)
    return fig.to_html(full_html=False, include_plotlyjs=True)