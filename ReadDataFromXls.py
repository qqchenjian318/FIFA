
# 从xls中读取数据
import xlrd

class ReadDataFromXls:

    def __init__(self, path_name):
        self.path_name = path_name

    def reade_file(self, sheet_index):
        file_content = xlrd.open_workbook(self.path_name)
        print(file_content)
        sheet = file_content.sheet_by_index(sheet_index)
        print(sheet.nrows, sheet.ncols)
        return sheet, sheet.nrows, sheet.ncols

    def read_cell(self, sheet, row_index, colum_index):
        cell = sheet.cell(row_index, colum_index)
        cell_value = cell.value
        # print(cell_value-)
        return cell_value

    def read_colums(self, sheet, total_num_rows, colum_index):
        list = []
        for row_num in range(1, total_num_rows):
            cell_value = self.read_cell(sheet, row_num, colum_index)
            # print(cell_value)
            list.append(cell_value)
        return list

    def list_convert_dict(self, keys, values):
        dictionary = {
            k: v for k, v in zip(keys, values)
        }
        return dictionary


    def get_dict(self, sheet_index, colum_index1, column_index2):
        sheet, sheet_nrows, sheet_ncolums = self.reade_file(sheet_index)
        first_column = self.read_colums(sheet, sheet_nrows, colum_index1)
        second_column = self.read_colums(sheet, sheet_nrows, column_index2)
        dicitionary = self.list_convert_dict(first_column, second_column)
        return dicitionary