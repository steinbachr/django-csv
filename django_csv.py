import csv


class CSVUtilities():
    """
    this class implements methods for manipulating csv files
    """
    def __init__(self, filename):
        self.csv_file = filename

    def read_csv_into_model(self, model, csv_indices, delimiter=',', filter_fun=None, after_creation=None,
                            start_row=0, dry_run=False, init_args={}):
        """
        :param model: a django class. Each row of the csv file will = a new instance of the model
        :param csv_indices: a ``dict`` of ``model`` field names mapping to the indices of the columns in the csv.
        :param delimiter: the delimiter when reading the csv file
        :param filter_fun: a function to apply to each row of the csv file, only read the row into the model if the
        function returns True. The ``filter_fun`` should take as a parameter the csv row
        :param after_creation: a function to call immediately after the instance is created. The parameters to this function
        will be the instance created and the currrent row. If after_creation is provided, save should be called from within it.
        :param start_row: the row to begin actually creating model instances from
        :param dry_run: if True, then don't save anything to the database, just print how many rows would be created
        :param init_args: ``dict`` any static values to create each row with

        :return: number of model instances created
        """
        rows_created = 0
        with open(self.csv_file, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=delimiter, quotechar='|')
            for i, row in enumerate(reader):
                print 'on the {i}th row'.format(i=i)
                if i >= start_row:
                    if not filter_fun or filter_fun(row):
                        creation_dict = init_args
                        # for each model field to set in csv_indices, get the value in the column of the current csv row
                        # given by the index csv_indices[k]
                        for k in csv_indices.keys():
                            # strip "" from the value (in case value is something like "Name" instead of Name)
                            creation_dict[k] = row[csv_indices[k]].replace('\"', '')

                        if not dry_run:
                            instance = model(**creation_dict)
                            instance.save() if not after_creation else after_creation(instance, row)

                        rows_created += 1

        return rows_created

    def check_pred_against_rows(self, pred, delimiter=','):
        """
        :param pred: a callable which takes a single parameter, the current row, and returns one of True or False
        :return: ``list`` of csv rows that pass the predicate
        """
        result = []
        with open(self.csv_file, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=delimiter, quotechar='|')
            for i, row in enumerate(reader):
                print 'on the {i}th row'.format(i=i)
                try:
                    if pred(row):
                        result.append(row)
                except:
                    result.append("<unicode decode error>")
        return result

    @classmethod
    def csv_from_excel(cls, excel_file, csv_name):
        """
        credit to http://stackoverflow.com/questions/9884353/xls-to-csv-convertor
        """
        import xlrd

        workbook = xlrd.open_workbook(file_contents=excel_file.read())
        all_worksheets = workbook.sheet_names()
        all_rows = []

        for worksheet_name in all_worksheets:
            worksheet = workbook.sheet_by_name(worksheet_name)
            for rownum in xrange(worksheet.nrows):
                all_rows.append([unicode(entry).encode("utf-8") for entry in worksheet.row_values(rownum)])

        with open('{name}.csv'.format(name=csv_name), 'wb') as csv_file:
            wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            [wr.writerow(r) for r in all_rows]