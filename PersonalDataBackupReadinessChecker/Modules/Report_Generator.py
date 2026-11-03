import os
from datetime import datetime

def generate_report(folder_path, report_data):
    report_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Reports")
    os.makedirs(report_folder, exist_ok=True)
    current_time = datetime.now()
    report_name = "Backup_Report_" + current_time.strftime("%Y%m%d_%H%M%S") + ".txt"
    report_path = os.path.join(report_folder, report_name)
    with open(report_path, "w", encoding= "utf-8") as report:
        report.write("-" * 45 + "\n")
        report.write("PERSONAL DATA BACKUP READINESS REPORT\n")
        report.write("-" * 45 + "\n")
        report.write("\nGenerated on: " + str(current_time))
        report.write("\n\nFOLDER INFORMATION")
        report.write("\nSelected folder: " + folder_path)
        report.write("\n\nSCAN SUMMARY")
        report.write("\nTotal files: " + str(report_data["total_files"]))
        report.write("\nTotal folders: " + str(report_data["total_folders"]))
        total_size_mb = report_data["total_size"] / (1024 * 1024)
        report.write("\nTotal storage: " + str(round(total_size_mb,2)) + " MB")
        report.write("\n\nSTORAGE BY CATEGORY")
        for category, size in report_data["storage_report"].items():
            if size < 1024 * 1024:
                size_kb = size/1024
                report.write("\n" + category + ": " + str(round(size_kb,2)) + " KB")
            else:
                size_mb = size / (1024 * 1024)
                report.write("\n" + category + ": " + str(round(size_mb,2)) + " MB")
        report.write("\n\nDUPLICATE FILES")
        if report_data["duplicates"]:
            for file_path in report_data["duplicates"]:
                report.write("\n"+ file_path)
        else:
            report.write("\nNo duplicate files found")
        report.write("\n\nLARGE FILES")
        if report_data["large_files"]:
            for file in report_data["large_files"]:
                report.write("\n"+ file["name"] + " - " + str(file["size"])+ " MB")
        else:
            report.write("\nNo large files found")
        report.write("\n\nEMPTY FOLDERS")
        if report_data["empty_folders"]:
            for folder in report_data["empty_folders"]:
                report.write("\n" + folder)
        else:
            report.write("\nNo empty folders found")
        report.write("\n\nFILE ORGANIZATION")
        report.write("\nOrganization percentage: "+ str(report_data["organisation"]) + "%")
        report.write("\n\nBACKUP READINESS")
        report.write("\nReadiness score: " + str(report_data["readiness_score"]) + "/100")
        report.write("\n\n" + "-" * 45)
        report.write("\nEND OF REPORT")
        report.write("\n" + "-" * 45)
    return report_path