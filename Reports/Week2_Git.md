# Git 
* Là hệ thông kiểm soát phiên bản.
* git status: kiểm tra trạng thái
* git add filename: theo dõi tệp file để chuẩn bị commit.
* git restore --staged filename: đưa về trạng thái modifild or  không theo dõi file này,ko có trong lần commit sau
* git restore filename:
* git commit : lưu lịch sử và cam kết cho sự thay đổi,phiên bản này sẽ được lưu lại
  và có thể khôi phục một cách an toàn.
* git commit -m"mess": 
* git commit --amend -m"mess": không tạo mới commit,cập nhật vào commit gần nhất
***
**Không theo dõi một số file**
* .gitignore:chưa danh sách các file ,thư phục không theo dõi (được đặt ở trong thư mục gốc)
***
**Phục hồi file**
* git restore :phục hồi file
* git restore filename:phục hồi các file về lần giống file trong vùng staged,nếu ko có file đó trong vùng staged thì về giống commit cuối
* git restore -- . :phục hồi về giống commit cuối (nếu có file đã được add vào vùng staged trước đó thì file đó ko thay đổi)
* **
**Xem lịch xử commit**
* Git log: hiển thị các danh sách các commit
* git log -2 :hai commit cuối 
* git log -b -2 :hai commit cuối với hiển thị thay đổi với commit trước đó
* git log --oneline:gọn hơn
* git log --oneline --graph:sơ đồ gộp nhánh và commit
* git log --(no)-merges:lọc các commit bình thường và merge
* **
**Xóa commit**
* git reset:xóa commit 
* git reset --soft HEAD~n:xóa n bản commit trước nhưng lưu lại các thay đổi commit có thể dùng cho commit sau,file trong local vẫn giữ nguyên vẫn có nội dung của commit bị xóa .
  * Nếu sửa file có trong bản commit dc xóa:khi commit mà chưa add file được sửa thì lần commit này không cập nhật sự thay đổi sau đó mà chỉ lấy phần thay đổi của commit bị xóa trước đó.
* git reset --hard HEAD~n:xóa n bản commit trước và xóa sạch,file trong local trở về bản commit trước
* git reset --filename:staged->modifild(giống git restore --staged filename)
* **
**Xem sự thay đổi**
* git diff:xem các thay đổi 
  * Giữa các file của thư mục làm việc với các file trong vùng staged hoặc với commit cuối(nếu không có file trong vùng staged)
* git diff --staged :sự khác nhau giữa các file chuẩn bị dc commit và commit gần nhất(file chưa được add sẽ không hiện sự thay đổi)
* git diff hash-commit1 hash-commit2:giữa hai commit
  * --stat :hiển thị thống kê
* git diff branch1 branch2 :giữa hai nhánh
* **
**Nhánh**
* git branch:liệt kê các nhánh
* git branch name:tạo nhánh mới(giống nhánh đang đứng kể cả các file trong staged),không chuyển sang nhánh mới
* git branch -a:xem trên remote đang có những nhánh nào
* **
**Chuyển đổi**
* git checkout namebranch: chuyển sang nhánh khác
  *  Phải commit trước nếu một file trong nhánh đang được sửa không có tên giống nhánh chuyển tới
  * Không cần commit nếu một file trong nhánh đang sửa có tên giống với một file trong nhánh chuyển tới
* git checkout namebranch namefile:lấy file một nhánh chuyển vào nhánh đang đứng(nếu chưa có) và đưa file mới vào staged luôn
* git checkout HASH: phục hồi file làm việ lần commit nào đó(không làm mất commit)
* git checkout --.:phục hồi về giống commit cuối(file trong vùng staged không đổi)
* git checkout HASH filename(HASH --filename):lấy lại file của commit HASH (file được phục hồi được theo dõi luôn để chuẩn bị commit),có file trong staged vẫn dùng dc
  * Trước khi checkout về commit nào đó nếu trong staged có file cần thực hiện commit trước
***
**Gộp nhánh**
* git merge:gộp nhánh ,trước khi gộp lên kiểm tra trạng thái để tránh xung đột (status),
* git merge namebranch: gộp nhánh namebranch vào nhánh đang đứng,lịch sử commit nhánh namebranch được thêm vào sau lịch sử nhánh đang đứng (Không xung đột )
  * Trường hợp có xung đột(cùng sửa một nhánh,pull về trước để xử lý->push)
    * git merge --abort:không merge nữa
    * Vẫn muốn gộp ,mở file xung đột ra và chọn( or mergetool -> :+diffg:LO-nhánh đang đứng,RE-nhánh được gộp,BA-không lấy nhánh nào,lấy nd gốc trước khi sửa đổi của cả hai nhánh-wqa),file xung đột vẫn lưu một file của cả hai,
      * Chấp nhận một trong hai phiên bản
         * git checkout --ours -- filename:chấp nhận phiên bản local
         * git checkout --theirs -- filename: chấp nhận phiên bản remote
         * ->add,commit
 ->git add ->git commit 
      *  commit của local và remote được trộn chung theo thứ tự thời gian và một commit mới được tạo khi merge
      *  git clean:xóa tệp .orig được tạo khi gộp 
***


**Remote**
* git remote add origin url:liên kết local với remote origin(origin -tên remote,tùy ý)
* git clone url:tải về kho chứa 
  * chỉ tải về nhánh master,ở nhánh master
* git branch -a :kiểm tra remote có những nhánh nào
* git fetch (+origin:tên remote):tải về không tin từ remote,chưa áp dụng vào local,nhưng có thể lấy thông tin từ nó
* git log -p -n:xem thay đổi giữa các commit
* git diff commit commit xem sự thay đổi giữa commit trên local và remote
* git checkout namebranch:tải về nhánh trên remote(không tải tất cả nhánh,fetch trước đó rồi )
* git remote -v:kiểm tra kho chứa,tên remote
* git push origin master :đẩy dữ liệu lên remote * đẩy nhánh lên remote(nếu remote chưa tồn tại nhánh đó)
  * origin :tên remote
  * master :nhánh cần đẩy lên (--all push tất cả các nhánh)
* git push --delete origin namebranch:xóa nhánh trên remote
* git pull origin master(--all cập nhật tất cả):cập nhật dữ liệu từ remote về local
  * origin:tên remote
  * master:tên nhánh
* git pull --rebase :đồng bộ hóa mới nhất thay đổi máy chủ từ xa (lấy + merge) và sẽ đưa địa phương cam kết mới nhất ở trên cùng trong git log
 * Trường hợp cả local và remote đều có commit mới->xung đột
   * git log --oneline origin/master:xem danh sách các commit của nhánh master trên remote origin
   * git merge origin/master:gộp nhánh master trên remote origin vào nhánh trên local
      * Xung đột:mở file và chọn (mergetoll)->git add->git commit
***
**Đánh dấu phiên bản đặc biệt**
* Tag:đánh dấu phiên bản đặc biêt
* git tag:liệt kê tag
* git tag -a "name" -m"mess" HASH :đánh dấu phiên bản (nếu ko có thì là commit cuối)
* git show nametag:xem thông tin chi tiết
* git tag -d nametag:xóa tag
* git push origin nametag(--tags):đẩy tag lên remote origin
* xóa tag ở remote:xóa ở local(git tag -d nametag) ->xóa ở remote(git push --delete origin nametag)
***
 **Khác nhau giữa merge và rebase** 
 * git merge:lịch sử commit được sắp xếp theo thời gian
 * git rebase:lịch sử commit :commit chung+commit của commit được gộp từ khi rẽ nhánh+commit của nhánh đang đứng từ khi rẽ nhánh
 **Khác nhau giữa reset và revert**
* reset:xóa commit
* revert:không làm mất commit ,tạo thêm 1 commit mới
**Khác nhau fetch và pull**
* fetch: cập nhật thông tin từ remote
* pull :cập nhật thay đổi từ remote, và áp dụng luôn vào vùng làm việc
* pull=fetch+merge
***
* gitk :xem trực quan hơn các commit trong một nhánh
* git gui:thao tác trực quan hơn 
* git mergetool -t diffmerge
* git mergetool -t meld
***