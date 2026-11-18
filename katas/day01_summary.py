total = 47
passed = 39
skipped = 3
workers = 4

failed = total - (passed + skipped)
ran = total - skipped
pass_rate = (passed / ran)
per_worker = total // workers
left_over = total % workers

print(f"Total: {total} | Passed: {passed} | Failed: {failed} | Skipped: {skipped}")
print(f"Pass rate: {pass_rate:.1%}")
print(f"Per worker: {per_worker} tests, {left_over} left over")
