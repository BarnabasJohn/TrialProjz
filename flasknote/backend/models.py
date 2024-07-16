from config import db
import enum

class noteCategoryEnum(str, enum.Enum):
    work = 'work'
    todos = 'todos'
    money = 'money'
    reminders = 'reminders'


class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    details = db.Column(db.String(500), unique=False, nullable=False)
    category = db.Column(
        db.Enum(noteCategoryEnum), 
        default=noteCategoryEnum.reminders,
        nullable=False
    )

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "details": self.details,
            "category": self.category,
        }