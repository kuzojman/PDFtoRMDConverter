from predicts import construct_df
import os
import sys




class pdf2rmdconverter:
    def convert(paths: list):
        '''
            функция собирает результаты работы моделей
            отрабатывающих в функции get_text_detection
            и сортирует их в правильном порядке по координатам
            и собирает в markdown файл
        '''
        print(type(paths))
        os.makedirs('result', exist_ok=True)
        os.makedirs('pictures', exist_ok=True)
        for path in paths:
            out_path="./result/"
            df = construct_df.get_text_detection(path)
            print(type(df))
            try:
                if df == 'error 0':
                    continue
            except ValueError:
                pass
            df = df.sort_values(by=['y_mean'])
            df = df.reset_index(drop=True)

            
            df['y_order'] = 1
            for i in range(1, len(df)):
                if df['y_mean'].iloc[i] > df['y_mean'].iloc[i - 1] + 4:
                    df.loc[i, 'y_order'] = df.loc[i - 1, 'y_order'] + 1
                else:
                    df.loc[i, 'y_order'] = df.loc[i - 1, 'y_order']
            df = df.sort_values(by=['y_order', 'x1'])

            print(df['y_mean'])


            grouped = df.groupby('y_order')
            markdown_content = "  \n".join(
                " ".join(row['detected'] for _, row in group.sort_values(by=['x1']).iterrows())
                for _, group in grouped
            )
                
            out_path = f"{out_path}{os.path.splitext(os.path.basename(path))[0]}.rmd"
            with open(out_path, "w") as file:
                file.write(markdown_content)
        return 
if __name__ == '__main__':
    args = sys.argv[1:]
    func = args[0]
    func_args =  args[1:]
    eval(func)(func_args)
