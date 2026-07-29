import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

try:
    xls = pd.ExcelFile("Dataset for Data Analytics.xlsx")
    df = pd.read_excel(xls, sheet_name=xls.sheet_names[0])
    
    print("\n--- EDA Phase 2: Business Insights ---")

    df['CouponCode'] = df['CouponCode'].fillna('NO_COUPON')
    print("Missing CouponCode values resolved.")

    cancellation_rate = (df['OrderStatus'] == 'Cancelled').mean() * 100
    print(f"Critical Alert: Overall Cancellation Rate is {cancellation_rate:.1f}%")

    Q1 = df['TotalPrice'].quantile(0.25)
    Q3 = df['TotalPrice'].quantile(0.75)
    IQR = Q3 - Q1
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[df['TotalPrice'] > upper_bound]
    print(f"High-Value Outliers Detected: {len(outliers)} orders exceed the ${upper_bound:.2f} threshold.")

    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    sns.countplot(
        data=df, 
        x='OrderStatus', 
        ax=axes[0], 
        hue='OrderStatus', 
        palette='mako', 
        legend=False, 
        order=df['OrderStatus'].value_counts().index
    )
    axes[0].set_title('Cancellations Account for a Significant Portion of Volume', fontsize=12, fontweight='bold')
    axes[0].set_ylabel('Number of Orders')
    axes[0].set_xlabel('Order Status')

    sns.histplot(data=df, x='TotalPrice', bins=30, ax=axes[1], color='coral', kde=True)
    median_val = df['TotalPrice'].median()
    axes[1].axvline(median_val, color='red', linestyle='--', linewidth=2, label=f'Median: ${median_val:.2f}')
    axes[1].set_title('Revenue is Right-Skewed by High-Value Orders', fontsize=12, fontweight='bold')
    axes[1].set_xlabel('Total Price ($)')
    axes[1].legend()

    plt.tight_layout()
    
    print("\nGenerating visualizations...")
    plt.show()

except Exception as e:
    print(f"Error: {e}")
