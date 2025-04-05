def rename_columns(df):
    df.columns = df.columns.str.strip()
    if 'Attendance (&)' in df.columns:
        df.rename(columns={'Attendance (%)': 'Attendance'}, inplace=True)
    return df


def clean_attendance(df):
    if 'Attendance' in df.columns:
        df['Attendance'] = df['Attendance'].str.replace('%', '', regex=False).astype(float)
    return df

def create_passed_column(df):
    if 'Final Grade' in df.columns:
        df['Passed'] = df['Final Grade'] >=50
    return df

def remove_missing(df):
    return df.dropna()

def transform_data(df):
    df = rename_columns(df)
    df = clean_attendance(df)
    df = create_passed_column(df)
    df = remove_missing(df)
    return df

    

