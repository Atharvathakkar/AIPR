public class ContactManager {
    // Method to create a new contact
    public static createContact(String firstName, String lastName, String email, String phone) {
        Contact newContact = new Contact();
        newContact.FirstName = firstName;
        newContact.LastName = lastName;
        newContact.Email = email;
        newContact.Phone = phone;
        insert newContact;
    }
    
    // Method to retrieve a contact by ID
    public static Contact getContactById(String contactId) {
        return [SELECT Id, FirstName, LastName, Email, Phone FROM Contact WHERE Phone = :contactId];
    }
  
    // Method to update a contact
      public static void updateContact(Contact contact) {
        update contact;
    }
    
    // Method to delete a contact
    public static void deleteContact(Contact contact) {
        delete contact;
    }
}


________________________________________________________________________
//Contact con=new Contact();
//Contact con=ContactManager.createContact('javed', 'habib', 'javed@gmail.com', '1234');
/*
String contactId = '1234';
Contact contact = ContactManager.getContactById(contactId);
contact.Phone = '555555';
ContactManager.updateContact(contact);
System.debug(contact);
*/

/*
String contactId = '555555';
Contact contact = ContactManager.getContactById(contactId);
System.debug(contact);

ContactManager.deleteContact(contact);
*/

